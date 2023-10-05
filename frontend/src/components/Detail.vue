<template>
  <div class="container my-3">
    <!-- 질문 -->
    <h2 class="border-bottom py-2">
      {{ question.subject }}
    </h2>
    <div class="card my-3">
      <div class="card-body">
        <!-- <div v-html="markdownToHtml"></div> -->
        <div class="card-text" v-html="marked.parse(question.content)"></div>
        <div class="d-flex justify-content-end">
          <div v-if="question.modify_date" class="badge bg-light text-dark p-2 text-start mx-3">
            <div class="mb-2">modified at</div>
            <div>{{moment(question.modify_date).format("YYYY년 MM월 DD일 hh:mm a")}}</div>
          </div>          
          <div class="badge bg-light text-dark p-2 text-start">
            <div class="mb-2">{{ question.user ? question.user.username : '' }}</div>
            <div>{{moment(question.create_date).format("YYYY년 MM월 DD일 hh:mm a")}}</div>
          </div>
        </div>
        <div class="my-3">
          <button class="btn btn-sm btn-outline-secondary"
            @click="voteQuestion(question.id)">추천
            <span class="badge rounded-pill bg-success">{{ question.voter.length }}</span>
          </button>                  
          <router-link class="btn btn-sm btn-outline-secondary" 
          v-if="question.user && store.username === question.user.username" 
          :to="{ name: 'question-modify', params: { question_id: question.id }}">수정</router-link>
          <button class="btn btn-sm btn-outline-secondary"
          v-if="question.user && store.username === question.user.username"
          @click="deleteQuestion()">삭제</button>
        </div>
      </div>
    </div>
    <button class="btn btn-secondary" @click="$router.push('/')">목록으로</button>

    <h5 class="border-bottom my-3 py-2">{{ question.answers.length }}개의 답변이 있습니다.</h5>
    <li v-for="answer in question.answers">
      <div class="card my-3">
        <div class="card body">
          <div class="card-text" style="white-space: pre-line;">{{ answer.content }}</div>
          <div class="d-flex justify-content-end">
                <div v-if="answer.modify_date" class="badge bg-light text-dark p-2 text-start mx-3">
                  <div class="mb-2">modified at</div>
                  <div>{{moment(answer.modify_date).format("YYYY년 MM월 DD일 hh:mm a")}}</div>
                </div>    
                <div class="badge bg-light text-dark p-2 text-start">
                  <div class="mb-2">{{ answer.user ? answer.user.username : '' }}</div>
                  <div>{{moment(answer.create_date).format("YYYY년 MM월 DD일 hh:mm a")}}</div>
                </div>
          </div>
          <div class="my-3">
            <button class="btn btn-sm btn-outline-secondary"
            @click="voteAnswer(answer.id)">추천
            <span class="badge rounded-pill bg-success">{{ answer?.voter?.length }}</span>
            </button>            
            <button class="btn btn-sm btn-outline-secondary"
            v-if="answer.user && store.username === answer.user.username"
            @click="$router.push({name : 'answer-modify', params : {answer_id : answer.id}})">수정</button>  
            <button class="btn btn-sm btn-outline-secondary"
            v-if="answer.user && store.username === answer.user.username"
            @click="deleteAnswer(answer.id)">삭제</button>     
          </div> 
        </div>
      </div>
    </li>

    <Error :error= "_error"/>
    <form method="post" class="my-3" @submit.prevent>

      <div class="mb-3">
        <textarea v-bind:disabled="!store.is_login" rows="10" v-model="content" class="form-control"></textarea>
      </div>
      <button type="submit" v-bind:disabled="!store.is_login" class="btn btn-primary" @click="postAnswer()">답변등록</button>
      
    </form>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue';
import { useRouter } from 'vue-router';
import fastapi from '../api/api'; // fastapi 모듈 경로를 수정해주세요.
import Error from './Error.vue'
import moment from 'moment/min/moment-with-locales'
import { useStore } from '../lib/store_pinia'
import { marked } from 'marked'
// import router from '../router/router';

moment.locale('ko')

const store = useStore()

const props = defineProps({
  question_id: String,
});

const question = ref({answers:[], voter:[], content:''});
const router = useRouter(); // useRoute 함수를 사용하여 $route 객체에 액세스
// const questionId = route.params.question_id
const questionId = props.question_id
// console.log("질문 id : " + route.params.question_id);
let content = ref("")
let _error = ref({})
console.log("content: " + content)

const postAnswer = async () => {
  console.log("post Answer - before")
  const operation = 'post';
  const url = '/api/answer/create/' + questionId; // FastAPI 엔드포인트 경로를 수정해주세요.
  const params = {content: content.value}; // 필요한 경우 요청 매개변수(params)를 설정하세요.

  
  try {
      fastapi(operation,url,params,
      (json) => {
          content = "";
          _error.value = {};
          fetchQuestion();
      },
      (error_json) => {
          console.error('Error fetching question list:', error_json.detail[0].msg);
          _error.value = error_json
          // console.log('error variable : ', _error.value.detail)

      }
      );
  } catch (error) {
      console.error('Error fetching question list:', error);
  }
};
  
const fetchQuestion = async () => {
  console.log("load Question")
  const operation = 'get';
  const url = '/api/question/detail/' + questionId; // FastAPI 엔드포인트 경로를 수정해주세요.
  const params = {}; // 필요한 경우 요청 매개변수(params)를 설정하세요.
  

try {
    fastapi(
    operation,
    url,
    params,
    (json) => {
        if (json) {
        question.value = json;
        }
    },
    (error) => {
        console.error('Error fetching question list:', error);
        // 에러 처리를 원하는 대로 수행하세요.
    }
    );
} catch (error) {
    console.error('Error fetching question list:', error);
    // 에러 처리를 원하는 대로 수행하세요.
}
};

const deleteQuestion = async () => {
  if (window.confirm("정말 삭제하시겠습니까?")){
    const url = "/api/question/delete"
    const params = {
      question_id : questionId
    }
    fastapi('delete', url, params,
    (json) => {
      router.push({name : "home"})
    },
    (error) => {
      _error.value = error
    })
  }
}

const deleteAnswer = async (answer_id) => {
  if (window.confirm("정말 삭제하시겠습니까?")){
    const url = "/api/answer/delete"
    const params = {
      answer_id : answer_id
    }
    fastapi('delete', url, params,
    (json) => {
      fetchQuestion()
    },
    (error) => {
      _error.value = error
    })
  }
}

const voteQuestion = async (_question_id) => {
  if (window.confirm("정말 추천하시겠습니까?")){
    const url = "/api/question/vote"
    const params = {
      question_id : _question_id
    }
    fastapi('post', url, params,
    (json) => {
      fetchQuestion()
    },
    (error) => {
      _error.value = error
    })
  }
}

const voteAnswer = async (_answer_id) => {
  if (window.confirm("정말 추천하시겠습니까?")){
    const url = "/api/answer/vote"
    const params = {
      answer_id : _answer_id
    }
    fastapi('post', url, params,
    (json) => {
      fetchQuestion()
    },
    (error) => {
      _error.value = error
    })
  }
}

onMounted(() => {
  fetchQuestion();
});
</script>
  
<style>
</style>
  
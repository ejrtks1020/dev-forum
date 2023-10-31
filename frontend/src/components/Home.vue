<template>
    <div class="container my-3">
         <div class="row my=3">
             <div class="col-6">
                 <button class="btn btn-primary" v-bind:disabled="!store.is_login" @click="$router.push('/question-create')">질문 등록하기</button>
             </div>
             <div class="col-6">
                 <div class="input-group">
                     <input type="text" class="form-control" v-model="kw">
                     <button class="btn btn-outline-secondary" @click="() => {store.keyword=kw, fetchQuestionList(0)}">찾기</button>
                 </div>
             </div>
         </div>
         <br>
         <table class="table">
             <thead>
             <tr class="text-center table-dark">
                 <th class="custom-th">조회수</th>
                 <th class="custom-th">번호</th>
                 <th class="custom-th" style="width:50%">제목</th>
                 <th class="custom-th">작성자</th>
                 <th class="custom-th">작성일자</th>
             </tr>
             </thead>
             <tbody>
             <tr class="text-center" v-for="question, index in questionList" :key="question.id">
                 <td class="custom-td">{{ question.view ? question.view : 0 }}</td>
                 <td class="custom-td">{{total - (store.page * size) - index}}</td>
                 <td class="text-start">
                 <router-link :to="{ name: 'detail', params: { question_id: question.id }}">
                     {{ question.subject }}
                 </router-link>
                 <span v-if="question.answers.length > 0" class="text-danger small mx-2">{{question.answers.length}}</span>
                 </td>
                 <!-- <td class="custom-td">{{ question.create_date }}</td> -->
                 <td>{{ question.user ? question.user.username : '' }}</td>
                 <td class="custom-td">{{moment(question.create_date).format("YYYY년 MM월 DD일 hh:mm a")}}</td>
             </tr>
             </tbody>
         </table>
     <!-- <a use:link href="/question-create" v-bind:disabled="store.is_login" class="btn btn-primary">질문 등록하기</a> -->
 
 
     <!-- 페이징처리 시작 -->
     <ul class="pagination justify-content-center">
         <!-- 이전페이지 -->
         <li v-if="store.page > 0" class="page-item">
         <button class="page-link" @click="fetchQuestionList(store.page - 1)">이전</button>
         </li>
 
         <li v-for="loop_page in total_page" :key="loop_page" class="page-item">
         <!-- {{ loop_page }} -->
         <button v-if="loop_page >= store.page-5 && loop_page <= store.page+5" class="page-link" :class="{ 'active': loop_page-1 === store.page }" @click="fetchQuestionList(loop_page-1)">{{ loop_page }}</button>
         </li>
 
         <!-- 다음페이지 -->
         <li v-if="store.page < total_page - 1" class="page-item">
         <button class="page-link" @click="fetchQuestionList(store.page + 1)">다음</button>
         </li>
     </ul>
     <!-- 페이징처리 끝 -->
 
     </div>
     
     <!-- <router-view /> -->    
     <!-- <ListTable :question-list="questionList"/> -->
     <!-- <router-view /> -->
 </template>
     
 <script setup>
 import { ref, onMounted, computed } from 'vue';
 import fastapi from '../api/api'; // fastapi 모듈 경로를 수정해주세요.
 // import ListTable from '../layouts/ListTable.vue';
 // import { useStore } from 'vuex'
 import { useStore } from '../lib/store_pinia'
 import moment from 'moment/min/moment-with-locales'
 moment.locale('ko')
 
 const questionList = ref([]);
 const size = ref(10);
 // const page = ref(0);
 const store = useStore();
 const total = ref(0);
 const total_page = ref(Math.ceil(total.value/size.value));
 console.log(store.username)
 
 const kw = ref('')
 
 
 
 const fetchQuestionList = async (_page) => {
 const operation = 'get';
 const url = '/api/question/list'; // FastAPI 엔드포인트 경로를 수정해주세요.
 const params = {
     page: _page,
     size: size.value,
     keyword: store.keyword
 }; // 필요한 경우 요청 매개변수(params)를 설정하세요.
 
 try {
     // fastapi 모듈을 사용하여 FastAPI 엔드포인트로 GET 요청 수행
     fastapi(
     operation,
     url,
     params,
     (json) => {
         if (json) {
         // 응답이 성공한 경우 데이터를 questionList에 할당
         questionList.value = json.question_list;
         total.value = json.total
         // store.getters.getPage = _page;
         kw.value = store.keyword
         store.page = _page;
         total_page.value = Math.ceil(total.value/size.value);
         }
         // console.log(total_page.value);
         console.log("current page : ", _page);
         console.log("is login : ", store.is_login)
 
         
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
 
 onMounted(() => {
     fetchQuestionList(store.page);
 });
 computed(() => {
     fetchQuestionList(store.page);
 })
 </script>
 
 <style>
 /* 스타일링을 추가할 수 있습니다. */
 </style>
       
<template>
  <div class="container my-3">
    <h2 class="border-bottom py-2">
      {{ question.subject }}
    </h2>
    <div class="card my-3">
      <div class="card-body">
        <div class="card-text" style="white-space: pre-line;">{{ question.content }}</div>
        <div class="d-flex justify-content-end">
          <div class="badge bg-light text-dark p-2">
            {{ question.create_date }}
          </div>
        </div>
      </div>
    </div>

    <h5 class="border-bottom my-3 py-2">{{ question?.answers?.length }}개의 답변이 있습니다.</h5>
    <ul v-for="answer in question.answers">
      <div class="card my-3">
        <div class="card body">
          <div class="card-text" style="white-space: pre-line;">{{ answer.content }}</div>
          <div class="d-flex justify-content-end">
                <div class="badge bg-light text-dark p-2">
                    {{answer.create_date}}
                </div>
          </div>          
        </div>
      </div>
    </ul>

    <ErrorView :error= "_error"/>
    <form method="post" class="my-3" @submit.prevent>

      <div class="mb-3">
        <textarea rows="10" v-model="content" class="form-control"></textarea>
      </div>
      <button type="submit" class="btn btn-primary" @click="postAnswer()">답변등록</button>
      
    </form>
  </div>
</template>

<script setup>
import ErrorView from './ErrorView.vue';

let content = ref("")


defineProps({
    question: Object,
    _error: Object,
})
</script>

<style>
</style>

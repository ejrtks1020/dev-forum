<template>
    <div class="container">
        <h5 class="my-3 border-bottom pb-2">질문 수정</h5>
        <Error :error="error" />
        <form method="post" class="my-3">
            <div class="mb-3">
                <label for="subject">제목</label>
                <input type="text" class="form-control" v-model="subject">
            </div>
            <div class="mb-3">
                <label for="content">내용</label>
                <textarea class="form-control" rows="10" v-model="content"></textarea>
            </div>
            <form method="post" class="my-3" @submit.prevent>
                <button type="submit" class="btn btn-primary" @click="updateQuestion()">수정하기</button>
            </form>
        </form>
    </div>
</template>

<script setup>
import fastapi from '../api/api';
import {ref} from 'vue';
import { useRouter } from 'vue-router'
import Error from './Error.vue'

const props = defineProps({
  question_id: String,
});

let subject = ref('')
let content = ref('')
let error = ref({})

const router = useRouter()

fastapi("get", "/api/question/detail/" + props.question_id, {},
            (json) => {
                subject.value = json.subject
                content.value = json.content
            })

const updateQuestion = async () => {
    const operation = 'put';
    const url = '/api/question/update'
    let params = {
        subject : subject.value,
        content : content.value,
        question_id : props.question_id
    }

    try {
        fastapi(operation, url, params,
            (json) => {
                console.log("Success Question Updating")
                router.push({name : 'detail', params : {question_id : props.question_id}})
            },
            (json_error) => {
                console.log("Fail Question Updating")
                error.value = json_error
            }
        )
    } catch (error) {
        console.error('Error fetching question list:', error);
    }
}

  
</script>

<style>
</style>
<template>
    <div class="container">
        <h5 class="my-3 border-bottom pb-2">답변 수정</h5>
        <Error :error="error" />
        <form method="post" class="my-3">
            <div class="mb-3">
                <label for="content">내용</label>
                <textarea class="form-control" rows="10" v-model="content"></textarea>
            </div>
            <form method="post" class="my-3" @submit.prevent>
                <button type="submit" class="btn btn-primary" @click="updateAnswer()">수정하기</button>
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
  answer_id: String,
});

const content = ref('')
const question_id = ref(0)
const error = ref({})

const router = useRouter()

fastapi("get", "/api/answer/detail/" + props.answer_id, {},
            (json) => {
                content.value = json.content
                question_id.value = json.question_id
            })

const updateAnswer = async () => {
    const operation = 'put';
    const url = '/api/answer/update'
    let params = {
        content : content.value,
        answer_id : props.answer_id
    }

    try {
        fastapi(operation, url, params,
            (json) => {
                console.log("Success Answer Updating")
                router.push({name : 'detail', params : {question_id : question_id.value}})
            },
            (json_error) => {
                console.log("Fail Answer Updating")
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
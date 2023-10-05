<script setup>
    import { useRouter } from 'vue-router'
    import Error from './Error.vue'
    import fastapi from '../api/api';
    import { ref } from 'vue'

    const router = useRouter()


    let error = ref({})
    let username = ''
    let password1 = ''
    let password2 = ''
    let email = ''

    const postUser = async () => {
        const operation = "post";
        const url = "/api/user/create"
        const params = {
            username: username,
            password1: password1,
            password2: password2,
            email: email
        }

        fastapi(operation, url, params,
        (json) => {
            router.push({name : "home"})
        },
        (json_error) => {
            error.value = json_error
        })

    }
</script>

<template>
    <div class="container">
        <h5 class="my-3 border-bottom pb-2">회원 가입</h5>
        <Error :error="error" />
        <form method="post" @submit.prevent>
            <div class="mb-3">
                <label for="username">사용자 이름</label>
                <input type="text" class="form-control" id="username" v-model="username">
            </div>
            <div class="mb-3">
                <label for="password1">비밀번호</label>
                <input type="password" class="form-control" id="password1" autocomplete="on" v-model="password1">
            </div>
            <div class="mb-3">
                <label for="password2">비밀번호 확인</label>
                <input type="password" class="form-control" id="password2" autocomplete="on" v-model="password2">
            </div>
            <div class="mb-3">
                <label for="email">이메일</label>
                <input type="text" class="form-control" id="email" v-model="email">
            </div>
            <button type="submit" class="btn btn-primary" @click="postUser()">생성하기</button>
        </form>
    </div>    
</template>

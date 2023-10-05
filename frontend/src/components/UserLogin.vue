<script setup>
    import { useRouter } from 'vue-router'
    import fastapi from "../api/api"
    import Error from "./Error.vue"
    import { ref } from "vue"
    import { useStore } from "../lib/store_pinia"
    // import { useStore } from "vuex"

    const router = useRouter()
    const error = ref({})
    const store = useStore()

    let login_username = ""
    let login_password = ""

    const login = async () => {
        const operation = "login"
        let url = "/api/user/login"
        let params = {
            username: login_username,
            password: login_password,
        }
        fastapi(operation, url, params, 
            (json) => {
                store.$patch({
                    page: store.$state.page,
                    access_token : json.access_token,
                    username: json.username,
                    is_login: true})
                router.push({name : "home"})
            },
            (json_error) => {
                error.value = json_error
            }
        )
    }
</script>

<template>
    <div class="container">
        <h5 class="my-3 border-bottom pb-2">로그인</h5>
        <Error :error="error" />
        <form method="post" @submit.prevent>
            <div class="mb-3">
                <label for="username">사용자 이름</label>
                <input type="text" class="form-control" id="username" v-model="login_username">
            </div>
            <div class="mb-3">
                <label for="password">비밀번호</label>
                <input type="password" class="form-control" id="password" autocomplete="on" v-model="login_password">
            </div>
            <button type="submit" class="btn btn-primary" @click="login()">로그인</button>
        </form>
    </div>
</template>


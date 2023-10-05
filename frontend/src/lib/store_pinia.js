import { defineStore } from 'pinia';
import {ref} from 'vue'

export const useStore = defineStore('myStore',() => {
    const page = ref(0)
    const keyword = ref('')
    const access_token = ref('')
    const username = ref('')
    const is_login = ref(false)

    // const getPage = computed(() => page.value)
    // const getAccessToken = computed(() => access_token.value)
    // const getUsername = computed(() => username.value)
    // const getIsLogin = computed(() => is_login.value)

    // function setPage (value) {page.value = value}
    // function setAccessToken (value) {access_token.value = value}
    // function setUsername (value) {username.value = value}
    // function setIsLogin (value) {is_login.value = value}
    return {page, keyword, access_token, username, is_login}
},
{
    persist : true,
    // storage: localStorage
});
export default useStore;
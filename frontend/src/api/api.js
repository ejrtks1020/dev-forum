import qs from "qs"
import { useStore } from "../lib/store_pinia"
import { useRouter } from "vue-router"

const fastapi = (operation, url, params, success_callback, failure_callback) => {
    let method = operation
    let content_type = 'application/json'
    let body = JSON.stringify(params)

    if (operation === 'login') {
        method = 'post'
        content_type = 'application/x-www-form-urlencoded'
        body = qs.stringify(params)
    }

    let _url = import.meta.env.VITE_SERVER_URL+url
    if(method === 'get') {
        _url += "?" + new URLSearchParams(params)
    }

    let options = {
        method: method,
        headers: {
            "Content-Type": content_type
        }
    }
    const store = useStore()
    // const router = useRouter()
    const _access_token = store.access_token
    if (_access_token) {
        options.headers['Authorization'] = 'Bearer ' + _access_token
    }

    if (method !== 'get') {
        options['body'] = body
    }
    fetch(_url, options)
        .then(response => {
            if(response.status == 204){
                if(success_callback){
                    success_callback()
                }
                return
            }
            response.json()
                .then(json => {
                    if(response.status >= 200 && response.status < 300) {  // 200 ~ 299
                        if(success_callback) {
                            success_callback(json)
                        }
                    }else if (operation !== 'login' && response.status === 401) { // token time out
                        store.$state.access_token = ''
                        store.$state.username = ''
                        store.$state.is_login = ''
                        alert("로그인이 필요합니다.")
                        failure_callback(json)
                        // router.push({name : 'user-login'})


                    }else {
                        if (failure_callback) {
                            failure_callback(json)
                        }else {
                            alert(JSON.stringify(json))
                        }
                    }
                })
                .catch(error => {
                    alert(JSON.stringify(error))
                })
        })
}

export default fastapi

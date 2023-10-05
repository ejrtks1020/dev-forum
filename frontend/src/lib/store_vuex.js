import {createStore} from 'vuex'
// Create a new store instance.
const store = createStore({
    state: {
        page: 0,
        access_token: "",
        username: "",
        is_login: false
      },
    getters: {
        getPage: state => {
            return state.page
        },
        getAccessToken: state => {
            return state.access_token
        },
        getUsername: state => {
            return state.username
        },
        getIsLogin: state => {
            return state.is_login
        }
    },
    mutations: {
        setPage (state, page){
            state.page = page;
        },
        setAccessToken(state, value) {
            state.access_token = value
        },
        setUsername(state, value) {
            state.username = value
        },
        setIsLogin(state, value) {
            state.is_login = value
        }     
    }
});

export default store;
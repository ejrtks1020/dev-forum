import { createRouter, createWebHistory } from 'vue-router'
import Home from "../components/Home.vue"
import Detail from "../components/Detail.vue"
import QuestionCreate from "../components/QuestionCreate.vue"
import UserCreate from "../components/UserCreate.vue"
import UserLogin from "../components/UserLogin.vue"
import QuestionModify from "../components/QuestionModify.vue"
import AnswerModify from "../components/AnswerModify.vue"


const router = createRouter({
    history: createWebHistory(),
    routes: [
        { path: '/', name:'home', component: Home },
        { path: '/detail/:question_id', name:'detail', component: Detail, props:true},
        { path: '/question-create', name:'question-create', component: QuestionCreate},
        { path: '/user-create', name:'user-create', component: UserCreate},
        { path: '/user-login', name:'user-login', component: UserLogin},
        { path: '/question-modify/:question_id', name:'question-modify', component:QuestionModify, props:true},
        { path: '/answer-modify/:answer_id', name:'answer-modify', component:AnswerModify, props:true}

    ]
})

export default router
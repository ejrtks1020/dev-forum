<script setup>
import { useRouter } from "vue-router";
const router = useRouter();

defineProps({
  questionList: Array
});

</script>

<template>
    <div class="container my-3">
        <table class="table">
            <thead>
            <tr class="table-dark">
                <th class="custom-th">번호</th>
                <th class="custom-th">제목</th>
                <th class="custom-th">작성일자</th>
            </tr>
            </thead>
            <tbody>
            <tr v-for="question, index in questionList" :key="question.id">
                <td class="custom-td">{{question.id}}</td>
                <td class="custom-td">
                <router-link :to="{ name: 'detail', params: { question_id: question.id }}">
                    {{ question.subject }}
                </router-link>
                </td>
                <td class="custom-td">{{ question.create_date }}</td>
            </tr>
            </tbody>

        </table>
        <button class="btn btn-primary" @click="$router.push('question-create')">질문 등록하기</button>
        <!-- <a use:link href="/question-create" class="btn btn-primary">질문 등록하기</a> -->

    </div>
    
    <!-- <router-view /> -->
</template>

<style scoped></style>
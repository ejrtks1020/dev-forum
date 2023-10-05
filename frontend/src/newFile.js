import fastapi from './api/api';

export default {
mounted() {
this.fetchQuestionList();
},
data() {
return {
questionList: [],
};
},
methods: {
async fetchQuestionList() {
const operation = 'get';
const url = "/api/question/list"; // FastAPI 엔드포인트 경로를 수정해주세요.
const params = {}; // 필요한 경우 요청 매개변수(params)를 설정하세요.

try {
// fastapi 모듈을 사용하여 FastAPI 엔드포인트로 GET 요청 수행
fastapi(
operation,
url,
params,
(json) => {
if (json) {
// 응답이 성공한 경우 데이터를 questionList에 할당
this.questionList = json;
}
},
(error) => {
console.error('Error fetching question list:', error);
// 에러 처리를 원하는 대로 수행하세요.
}
);
} catch (error) {
console.error('Error fetching question list:', error);
// 에러 처리를 원하는 대로 수행하세요.
}
},
},
};

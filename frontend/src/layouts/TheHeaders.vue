

<template>
    <header>
        <nav class="navbar navbar-expand-lg navbar-light bg-light">
            <div class="container-fluid">
                <a use:link class="navbar-brand" href='/' @click="() => {store.keyword = '', store.page = 0}">FastVue</a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent.collapse" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarSupportedContent">
                    <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                        <li v-if="store.is_login">
                            <li class="nav-item">
                                <a use:link class="nav-link" href='/user-login' @click="() => {
                                    store.$patch({
                                        page: store.page,
                                        access_token : '',
                                        username: '', 
                                        is_login: false})
                                }">로그아웃 {{ store.username }}</a>
                            </li>
                        </li>

                        <li v-else>
                            <li class="nav-item">
                            <router-link :to="{ name: 'user-create'}" class="nav-link active" aria-current="page">회원가입</router-link>
                            <!-- <a class="nav-link active" aria-current="page" href="#">회원가입</a> -->
                            </li>
                            <li class="nav-item">
                            <router-link :to="{ name: 'user-login'}" class="nav-link">로그인</router-link>
                            <!-- <a class="nav-link" href="#">로그인</a> -->
                            </li>
                        </li>
                        <!-- <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                            Dropdown
                        </a>
                        <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                            <li><a class="dropdown-item" href="#">Action</a></li>
                            <li><a class="dropdown-item" href="#">Another action</a></li>
                            <li><hr class="dropdown-divider"></li>
                            <li><a class="dropdown-item" href="#">Something else here</a></li>
                        </ul> -->
                        <!-- </li> -->
                        <!-- <li class="nav-item">
                        <a class="nav-link disabled" href="#" tabindex="-1" aria-disabled="true">Disabled</a>
                        </li> -->
                    </ul>
                <!-- <form class="d-flex">
                    <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
                    <button class="btn btn-outline-success" type="submit">Search</button>
                </form> -->
                </div>
            </div>
        </nav>
    </header>
</template>

<script setup>
// import { useStore } from 'vuex'
// const store = useStore();
import { useStore } from '../lib/store_pinia'
const store = useStore()
</script>

<style scoped></style>
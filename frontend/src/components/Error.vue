<template>
    <div>
        <li v-if="error">
            <li v-if="(typeof error.detail == 'string')">
                <div class="alert alert-danger" role="alert">
                    <div>
                        {{error.detail}}
                    </div>
                </div>

                <!-- {{error.detail}} -->
            </li>
            <li v-else-if="(typeof error.detail === 'object' && error.detail.length > 0)">
                <div class="alert alert-danger" role="alert">
                    <li v-for="err, i in error.detail">
                    <div>
                        <strong>{{err.loc[1]}}</strong> : {{err.msg}}
                    </div>
                </li>
                </div>

                <!-- <li v-for="err, i in error.detail">
                    <strong>{{err.loc[1]}}</strong> : {{err.msg}}
                </li> -->
            </li>
        </li>
    </div>
</template>


<script setup>
defineProps({
  error: Object
});
// console.log("Error.vue : ", props.error)
</script>
<template>
    <v-app>
        <div class="d-flex flex-column flex-sm-row h-screen">
            <div class="test">
                <v-img :width="mdAndUp? 700: 600" cover src="../../public/chat-isometric.png" class=""></v-img>
            </div>
            <v-sheet class="d-flex flex-column justify-sm-center pa-6" color="#ffff">
                <p class="text-h5 text-center font-weight-bold">Share your moments and thoughts. Everytime. Everywhere</p>
                <div class="d-flex mt-5 justify-center flex-sm-column align-sm-center">
                    <v-btn flat color="primary" to="/login" :class="smAndUp? 'w-100 mb-3': 'w-50 mr-2'">Login</v-btn>
                    <v-btn variant="outlined" to="/signup" color="primary" :class="smAndUp? 'w-100': 'w-50'">Sign up</v-btn>
                </div>
            </v-sheet>
        </div>
    </v-app>
</template>


<script setup>
import { useDisplay } from 'vuetify/lib/framework.mjs';

const { smAndUp, mdAndUp } = useDisplay();



</script>

<style scoped>
.test {
    height: 80vh;
    padding-top: 20vh;
}


@media only screen and (min-width: 768px) {
    .test {
        height: 100vh;
        padding-top: 30vh;
    }

}
@media only screen and (min-width: 992px) {
    .test {
        width: 90%;
        padding-top: 20vh;
        padding-left: 10vw;
    }
}

</style>
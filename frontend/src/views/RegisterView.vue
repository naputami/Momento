<template>
    <v-app>

        <ShowAlert activity="Account Registration" 
        :message="alertData.message" 
        :status="alertData.status"
        v-show="alertVisibility"/>

        <v-container class="mt-2" align="center">
            <h1 class="mt-8 heading">Create Account</h1>
            <v-sheet :width="smAndUp? '500' : '330'" class="mt-5 pa-6 pb-3" elevation="4" rounded="lg">
                <v-form @submit.prevent="handleRegis">
                    <v-text-field label="Name" placeholder="John Doe" type="text" v-model="userData.name"></v-text-field>
                    <v-text-field label="Email address" placeholder="johndoe@gmail.com" type="email" v-model="userData.email"></v-text-field>
                    <v-select
                    label="Select Your Role"
                    :items="['Admin', 'User']"
                    variant="outlined"
                    v-model="userData.role"
                    ></v-select>
                    <v-text-field label="Username" placeholder="johndoe" type="text" v-model="userData.username"></v-text-field>
                    <v-text-field label="Password" :type="showPassword? 'text': 'password'" :append-inner-icon="showPassword? mdiEyeOff : mdiEye" @click:append-inner="showPassword = !showPassword" v-model="userData.password"></v-text-field>
                    <v-text-field label="Retype password" :type="showRetypePassword? 'text': 'password'" :append-inner-icon="showRetypePassword? mdiEyeOff : mdiEye" @click:append-inner="showRetypePassword = !showRetypePassword"></v-text-field>
                    <div class="d-flex flex-column">
                        <v-btn type="submit" color ="primary">Sign Up</v-btn>
                    </div>
                    <v-card-text class="text-center">
                        <RouterLink
                        to="/login"
                        class="text-primary text-decoration-none"
                        >
                        Login now <v-icon :icon="mdiChevronDoubleRight"></v-icon>
                        </RouterLink>
                </v-card-text>
                </v-form>
            </v-sheet>
        </v-container>
    </v-app>
</template>

<script setup>
    import { ref, reactive } from 'vue';
    import { useDisplay } from 'vuetify/lib/framework.mjs';
    import { mdiChevronDoubleRight, mdiEye, mdiEyeOff } from "@mdi/js";
    import { RouterLink  } from 'vue-router';
    import { useAuth } from '../compostable/auth';
    import ShowAlert from '../components/showalert.vue';

    const { success, accountRegister, error, alertData, alertVisibility, hideAlert } = useAuth()
  
    const showPassword = ref(false);
    const showRetypePassword= ref(false);
    const { smAndUp } = useDisplay();

    const userData = reactive({
        name: '',
        username: '',
        email: '',
        password: '',
        role: ''
    })

    const handleRegis = async () => {
        await accountRegister('api/auth/signup', userData)

        console.log(success.value)

        if(success.value){
            alertData.message = success.value
            alertData.status = 'success'
            alertVisibility.value = true
            setTimeout(hideAlert, 3000)
        }

        if(error.value){
            alertData.message = error.value
            alertData.status = 'error'
            alertVisibility.value = true
            setTimeout(hideAlert, 3000)
        }
    }


</script>

<style scoped></style>
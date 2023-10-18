<template>
    <v-app>

      <ShowAlert activity="Login" 
        :message="alertData.message" 
        :status="alertData.status"
        v-show="alertVisibility"/>

      <v-container class="mt-2" align="center">
        <h1 class="mt-8 heading">Welcome Back!</h1>
          <v-sheet :width="smAndUp? '500' : '330'" class="mt-5 pa-6 pb-3" elevation="4" rounded="lg">
          <v-form @submit.prevent="handleLogin">
          <v-text-field label="Username" color="primary" prepend-inner-icon="$account" required v-model="loginData.username"></v-text-field>
          <v-text-field label="Password" :type="showPassword? 'text': 'password'"  
          prepend-inner-icon="$password" :append-inner-icon="showPassword? mdiEyeOff : mdiEye" 
          color="primary" @click:append-inner="showPassword = !showPassword" required v-model="loginData.password"></v-text-field>
          <div class="d-flex flex-column">
            <v-btn type="submit" color ="primary">Login</v-btn>
          </div>
        </v-form>
        <v-card-text class="text-center">
        <RouterLink
          to="/signup"
          class="text-primary text-decoration-none"
        >
          Sign up now <v-icon :icon="mdiChevronDoubleRight"></v-icon>
        </RouterLink>
      </v-card-text>
        </v-sheet>
      </v-container>
    </v-app>
  </template>
  
<script setup>
    import { ref } from 'vue';
    import { reactive } from 'vue';
    import { useDisplay } from 'vuetify/lib/framework.mjs';
    import { mdiChevronDoubleRight, mdiEye, mdiEyeOff} from '@mdi/js';
    import { RouterLink } from 'vue-router';
    import { useRouter } from 'vue-router';
    import {useAuth} from '../compostable/auth';
    import ShowAlert from '../components/showalert.vue';


  
    const showPassword = ref(false);
    const { smAndUp } = useDisplay();
    const router = useRouter();

    const loginData = reactive({
      username: '',
      password: ''
    });

    const { success, userLogin, error, alertData, alertVisibility, hideAlert } = useAuth()

    const handleLogin = async () => {
      await userLogin('api/auth/login', loginData)

      if(success.value) {
        router.push('/')
      }

      
      if(error.value){
            alertData.message = error.value
            alertData.status = 'error'
            alertVisibility.value = true
            setTimeout(hideAlert, 3000)
        }
    }

</script>

<style scoped>
</style>
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
                  <v-btn type="submit" color ="primary" :loading="loading">Login</v-btn>
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
    import { useAuthStore } from '../store/useAuthStore';
    import ShowAlert from '../components/showalert.vue';


  
    const showPassword = ref(false);
    const { smAndUp } = useDisplay();
    const router = useRouter();
    const loading = ref(false)

    const loginData = reactive({
      username: '',
      password: ''
    });

    const { success, userLogin, error, alertData, alertVisibility, hideAlert, accessToken, refreshToken, role, username } = useAuth();
    const {setToken, setUserData} = useAuthStore();

    const handleLogin = async () => {
      await userLogin('api/auth/login', loginData);
      loading.value = true;

      if(success.value) {
        setToken(accessToken.value, refreshToken.value);
        setUserData(username.value, role.value);
        router.push('/');
        loading.value = false;
      }

      
      if(error.value){
            alertData.message = error.value
            alertData.status = 'error'
            alertVisibility.value = true
            setTimeout(hideAlert, 3000)
            loading.value = false;
        }
    }

</script>

<style scoped>
</style>
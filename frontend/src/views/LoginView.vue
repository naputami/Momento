<template>
    <v-app>

      <v-container class="mt-2" align="center">
        <h1 class="mt-8 heading">Welcome Back!</h1>
          <v-sheet :width="smAndUp? '500' : '330'" class="mt-5 pa-6 pb-3" elevation="4" rounded="lg">
              <v-form @submit.prevent="handleLogin">
                <v-text-field label="Username" color="primary" prepend-inner-icon="$account" required v-bind="username"></v-text-field>
                <v-text-field label="Password" :type="showPassword? 'text': 'password'"  
                prepend-inner-icon="$password" :append-inner-icon="showPassword? mdiEyeOff : mdiEye" 
                color="primary" @click:append-inner="showPassword = !showPassword" required v-bind="password"></v-text-field>
                <div class="d-flex flex-column my-2">
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
    import { useDisplay } from 'vuetify/lib/framework.mjs';
    import { mdiChevronDoubleRight, mdiEye, mdiEyeOff} from '@mdi/js';
    import { RouterLink } from 'vue-router';
    import { useRouter } from 'vue-router';
    import {useForm} from 'vee-validate';
    import * as yup from 'yup';
    import Swal from 'sweetalert2';
    import {useAuth} from '../compostable/auth';
    import { useAuthStore } from '../store/useAuthStore';
  

  
    const showPassword = ref(false);
    const { smAndUp } = useDisplay();
    const router = useRouter();
    const loading = ref(false);

    const schema = yup.object({
      username: yup.string().required().label('Username'),
      password:  yup.string().required().label('Password')
    })


    const { handleSubmit, defineComponentBinds  } = useForm({
        validationSchema: schema
    
    });

    const vuetifyConfig = (state) => ({
        props: {
            'error-messages': state.errors,
        },
    });


    const { success, userLogin, error, accessToken, refreshToken, role, userAccount } = useAuth();
    const {setToken, setUserData} = useAuthStore();

    const username = defineComponentBinds('username', vuetifyConfig)
    const password = defineComponentBinds('password', vuetifyConfig);

    const handleLogin = handleSubmit(async values => {
      await userLogin('api/auth/login', values);
      loading.value = true;

      if(success.value) {
        setToken(accessToken.value, refreshToken.value);
        setUserData(userAccount.value, role.value);
        Swal.fire({
                      title: 'Login successfully!',
                      icon: 'success',
                      showConfirmButton: false,
                      timer: 2000
                  })
        router.push('/');
        loading.value = false;
        success.value = null;
      }

      
      if(error.value){
        Swal.fire({
                    title: 'Login Failed!',
                    text: `${error.value}`,
                    icon: 'error',
                    showConfirmButton: false,
                    timer: 3000
                  })
            loading.value = false;
            error.value = null;
        }
    })

</script>

<style scoped>
</style>
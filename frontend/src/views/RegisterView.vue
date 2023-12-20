<template>
    <v-app>

        <v-container align="center">
            <h1 class="mt-8 heading">Create Account</h1>
            <v-sheet :width="smAndUp? '500' : '330'" class="mt-5 pa-6 pb-3" elevation="4" rounded="lg">
                <v-form @submit.prevent="submit">
                    <v-text-field label="Name" placeholder="John Doe" type="text" v-bind="name" id="name"></v-text-field>
                    <v-text-field label="Email address" placeholder="johndoe@gmail.com" type="email" v-bind="email" id="email"></v-text-field>
                    <v-text-field label="Username" placeholder="johndoe" type="text" v-bind="username" id="username"></v-text-field>
                    <v-text-field label="Password" :type="showPassword? 'text': 'password'" :append-inner-icon="showPassword? mdiEyeOff : mdiEye" @click:append-inner="showPassword = !showPassword" v-bind="password" id="password"></v-text-field>
                    <v-text-field label="Retype password" :type="showRetypePassword? 'text': 'password'" :append-inner-icon="showRetypePassword? mdiEyeOff : mdiEye" @click:append-inner="showRetypePassword = !showRetypePassword" v-bind="passwordConfirm" id="passwordConfirm"></v-text-field>
                    <div class="d-flex flex-column my-2">
                        <v-btn type="submit" color ="primary">Sign Up</v-btn>
                        <v-btn color ="primary" variant="outlined" class="mt-2" @click="resetForm()">Clear Form</v-btn>
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
    import { ref } from 'vue';
    import { useDisplay } from 'vuetify/lib/framework.mjs';
    import { mdiChevronDoubleRight, mdiEye, mdiEyeOff } from "@mdi/js";
    import { RouterLink  } from 'vue-router';
    import {useForm} from 'vee-validate';
    import * as yup from 'yup';
    import Swal from 'sweetalert2';
    import { useAuth } from '../compostable/auth';


    const { success, accountRegister, error } = useAuth();
  
    const showPassword = ref(false);
    const showRetypePassword= ref(false);
    const { smAndUp } = useDisplay();

    const schema = yup.object({
        name: yup.string().required().label('Name'),
        username: yup.string().required().label('Username'),
        email: yup.string().email().required().label('E-mail'),
        password: yup.string().matches( /^(?=.*\d)(?=.*[a-zA-Z])(?=.*[@#$%^&+=!]).{8,}$/, "Password should at least 8 characters including capital letters, numbers, and special characters!").required(),
        passwordConfirm: yup
        .string()
        .oneOf([yup.ref('password')], 'Passwords must match')
        .required()
        .label('Password confirmation')
  });


    const { defineComponentBinds, handleSubmit, resetForm } = useForm({
        validationSchema: schema,
    });

    const vuetifyConfig = (state) => ({
        props: {
            'error-messages': state.errors,
        },
    });


    const name = defineComponentBinds('name', vuetifyConfig);
    const username = defineComponentBinds('username', vuetifyConfig)
    const email = defineComponentBinds('email', vuetifyConfig);
    const password = defineComponentBinds('password', vuetifyConfig);
    const passwordConfirm = defineComponentBinds('passwordConfirm', vuetifyConfig);


    const submit = handleSubmit( async values => {
   
        await accountRegister('api/auth/signup', values);

        if(success.value){
            Swal.fire(
                        {
                            title: 'Account Registration Success!',
                            text: `${success.value}`,
                            icon: 'success',
                            showConfirmButton: false,
                            timer: 3000
                        }
                    )
        }

        if(error.value){
            Swal.fire(
                        {
                            title: 'Account Registration Failed!',
                            text: `${error.value}`,
                            icon: 'error',
                            showConfirmButton: false,
                            timer: 3000
                        }
                    )

        }
    })


</script>

<style scoped></style>
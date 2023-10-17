<template>
    <v-app>
        <v-container class="mt-5" align="center">
            <h1 class="mt-16 heading">Create Account</h1>
            <v-sheet :width="smAndUp? '500' : '330'" class="mt-5 pa-6 pb-3" elevation="4" rounded="lg">
                <v-form>
                    <v-text-field label="Name" placeholder="John Doe" type="text"></v-text-field>
                    <v-text-field label="Email address" placeholder="johndoe@gmail.com" type="email"></v-text-field>
                    <v-text-field label="Username" placeholder="johndoe" type="text"></v-text-field>
                    <v-text-field label="Password" :type="showPassword? 'text': 'password'" :append-inner-icon="showPassword? mdiEyeOff : mdiEye" @click:append-inner="showPassword = !showPassword"></v-text-field>
                    <v-text-field label="Retype password" :type="showRetypePassword? 'text': 'password'" :append-inner-icon="showRetypePassword? mdiEyeOff : mdiEye" @click:append-inner="showRetypePassword = !showRetypePassword"></v-text-field>
                    <div class="d-flex flex-column">
                        <v-btn type="submit" color ="primary">Sign Up</v-btn>
                    </div>
                    <v-card-text class="text-center">
                        <a
                        class="text-primary text-decoration-none"
                        href="#"
                        rel="noopener noreferrer"
                        target="_blank"
                        >
                        Login now <v-icon :icon="mdiChevronDoubleRight"></v-icon>
                        </a>
                </v-card-text>
                </v-form>
            </v-sheet>
        </v-container>
    </v-app>
</template>

<script setup>
    import { ref } from 'vue'
    import { useDisplay } from 'vuetify/lib/framework.mjs';
    import { mdiChevronDoubleRight, mdiEye, mdiEyeOff } from "@mdi/js";
  
    const showPassword = ref(false);
    const showRetypePassword= ref(false);
    const { smAndUp } = useDisplay();

</script>

<style scoped></style>
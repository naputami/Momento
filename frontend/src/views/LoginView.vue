<template>
    <v-app>
      <v-container class="mt-16" align="center">
        <h2 class="mt-16 heading">Welcome Back!</h2>
          <v-sheet :width="mdAndUp? '500' : '330'" class="mt-5 pa-6 pb-3" elevation="4" rounded="lg">
          <v-form>
          <v-text-field label="Username" variant="outlined" color="primary" prepend-inner-icon="$account" required></v-text-field>
          <v-text-field label="Password" :type="showPassword? 'text': 'password'" variant="outlined"  
          prepend-inner-icon="$password" :append-inner-icon="showPassword? mdiEyeOff : mdiEye" 
          color="primary" @click:append-inner="showPassword = !showPassword" required></v-text-field>
          <div class="d-flex flex-column">
            <v-btn type="submit" color ="primary">Login</v-btn>
          </div>
        </v-form>
        <v-card-text class="text-center">
        <a
          class="text-primary text-decoration-none"
          href="#"
          rel="noopener noreferrer"
          target="_blank"
        >
          Sign up now <v-icon :icon="mdiChevronDoubleRight"></v-icon>
        </a>
      </v-card-text>
        </v-sheet>
      </v-container>
    </v-app>
  </template>
  
<script setup>
    import { ref } from 'vue'
    import { useDisplay } from 'vuetify/lib/framework.mjs';
    import { mdiChevronDoubleRight, mdiEye, mdiEyeOff,} from '@mdi/js'
  
    const showPassword = ref(false)
    const { mdAndUp } = useDisplay()

</script>

<style scoped>
</style>
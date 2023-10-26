<template>
        <v-navigation-drawer v-model="sidebar" color="primary" temporary>
        <v-list  density="compact" nav>
          <v-list-item prepend-icon="$home" title="Home" value="home"></v-list-item>
          <v-list-item prepend-icon="$crown" title="Leaderboard" value="leaderboard"></v-list-item>
          <v-list-item prepend-icon="$admin" title="Admin" value="admin"></v-list-item>
          <v-list-item prepend-icon="$logout" title="Logout" value="logout"></v-list-item>
        </v-list>
    </v-navigation-drawer>
    <v-app-bar color="primary" scroll-behavior="elevate">
        <span class="hidden-md-and-up">
            <v-app-bar-nav-icon @click="sidebar = !sidebar"></v-app-bar-nav-icon>
        </span>
        <v-toolbar-title>Momento</v-toolbar-title>
        <v-spacer></v-spacer>
        <div class="hidden-sm-and-down">
            <v-btn flat>
                <v-icon left dark icon="$home"></v-icon>
                Home
            </v-btn>
            <v-btn flat>
                <v-icon left dark icon="$crown"></v-icon>
                Leaderboard
            </v-btn>
            <v-btn flat>
                <v-icon left dark icon="$admin"></v-icon>
                Admin
            </v-btn>
            <v-btn variant="text" @click="handleLogout">
                <v-icon left dark icon="$logout"></v-icon>
                Logout
            </v-btn>
        </div>
    </v-app-bar>
</template>

<script setup>
import { ref } from 'vue';
import { useAuth } from '../compostable/auth';
import { useAuthStore } from '../store/useAuthStore';
import { useRouter } from 'vue-router';

const {userLogout, success, alertData, error} = useAuth();
const {removeToken, accessToken} = useAuthStore();
const sidebar = ref(false);
const router = useRouter();

const handleLogout = async () => {
    await userLogout('api/auth/logout', accessToken)

    if(success.value){
        removeToken();
        router.push('/login')
    }

    if(error.value){
        alertData.message = error.value
        alertData.status = 'error'
        alert(alertData.message)
    }
}
</script>

<!-- <style scoped>
.test {
    color: aqua;
}
</style> -->
<template>
        <v-navigation-drawer v-model="sidebar" color="primary" temporary>
        <v-list  density="compact" nav>
          <v-list-item prepend-icon="$home" title="Home" value="home" to="/home"></v-list-item>
          <v-list-item prepend-icon="$crown" title="Leaderboard" value="leaderboard" to="/leaderboard"></v-list-item>
          <v-list-item prepend-icon="$admin" title="Admin" value="admin" :href="urlAdmin" v-show="role === 'admin'"></v-list-item>
          <v-list-item prepend-icon="$logout" title="Logout" value="logout" @click="handleLogout"></v-list-item>
        </v-list>
    </v-navigation-drawer>
    <v-app-bar color="primary" scroll-behavior="hide">
        <span class="hidden-md-and-up">
            <v-app-bar-nav-icon @click="sidebar = !sidebar"></v-app-bar-nav-icon>
        </span>
        <v-toolbar-title>Momento</v-toolbar-title>
        <v-spacer></v-spacer>
        <div class="hidden-sm-and-down">
            <v-btn flat to="/home">
                <v-icon left dark icon="$home"></v-icon>
                Home
            </v-btn>
            <v-btn flat to="/leaderboard">
                <v-icon left dark icon="$crown"></v-icon>
                Leaderboard
            </v-btn>
            <v-btn flat :href="urlAdmin" v-show="role === 'admin'">
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
import Swal from 'sweetalert2';
import { useAuth } from '../compostable/auth';
import { useAuthStore } from '../store/useAuthStore';
import { usePostStore } from '../store/usePostStore';
import { useRouter } from 'vue-router';

const {userLogout, success, alertData, error} = useAuth();
const { removeUserData, role } = useAuthStore();
const {removePostData} = usePostStore();
const sidebar = ref(false);
const router = useRouter();
const urlAdmin = import.meta.env.VITE_API_BASE_URL + "/admin";

const handleLogout = async () => {
    Swal.fire({
        title: 'Logout Confirmation',
        text: 'Are you sure to logout?',
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#006d77ff',
        cancelButtonColor: '#cd858c',
        confirmButtonText: 'Yes',
    }).then(async result => {
        if(result.isConfirmed){
            await userLogout('api/auth/logout')

                if(success.value){
                    removeUserData();
                    removePostData();
                    Swal.fire({
                            title: 'Logout successfully!',
                            icon: 'success',
                            showConfirmButton: false,
                            timer: 2000
                        })
                    router.push('/login');
                    success.value = null;
                }

                if(error.value){
                    alertData.message = error.value
                    alertData.status = 'error'
                    Swal.fire(
                        {
                            title: 'Logout Failed!',
                            text: `${alertData.message}`,
                            icon: 'error',
                            showConfirmButton: false,
                            timer: 3000
                        }
                    )
                    error.value = null;
                }
        }
    })
   
}
</script>

<!-- <style scoped>
.test {
    color: aqua;
}
</style> -->
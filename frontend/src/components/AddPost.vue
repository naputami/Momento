<template>
      <v-btn @click="dialog = true" icon="$pencil" color="primary" size="x-large"> </v-btn>

        <v-dialog v-model=dialog width="500">
                <v-card title="Add New Post">
                <v-divider></v-divider>
                <form width="w-100" class="mt-5 pa-5" @submit.prevent="handleAddPost">
                    <v-file-input
                    chips
                    multiple
                    label="Add image (optional)"
                    variant="outlined"
                    prepend-icon="$camera"
                    v-model="formData.file"
                    ></v-file-input>
                    <v-textarea
                    label="Write your thougts here"
                    prepend-icon="$text"
                    variant="outlined"
                    v-model="formData.content"
                    ></v-textarea>
                    <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn text="Cancel" @click="dialog = false"></v-btn>
                    <v-btn variant="flat" type="submit" @click="dialog = false" text="Post" color="primary"></v-btn>
                    </v-card-actions>
                </form>
                </v-card>
            </v-dialog>
</template>

<script setup>
import { ref, reactive } from 'vue';
import { usePostStore } from '../store/usePostStore';
import { useFetch } from '../compostable/post';
import { storeToRefs } from "pinia";
import Swal from 'sweetalert2';


const {data, postTextOnly, postFile, success, error, totalItem} = useFetch();
const store = usePostStore();
const {postState} = storeToRefs(store);
const {setNewPost, setTotalItems} = store;


const Toast = Swal.mixin({
  toast: true,
  position: 'bottom',
  showConfirmButton: false,
  timer: 2500
})



const formData = reactive({
    content: '',
    file: ''
})

const handleAddPost = async () => {
    if(formData.file === ''){
        const content = {
            'content': formData.content
        }
        await postTextOnly('api/posts', content);

        if(success.value){
            setNewPost(data.value);
            setTotalItems(totalItem.value)
            formData.content = ''
            console.log('Post without file')
            console.log('this is post state', postState.value.posts)
            Toast.fire({
                icon: 'success',
                title: 'Post is successfully created!'
            })
            success.value = null;
        }

        if(error.value){
            Toast.fire({
                icon: 'error',
                title: `${error.value}`
            })
            error.value = null;
        }
       
    } else {
        const post = {
            'content': formData.content,
            'file': formData.file[0]
        }

        await postFile('api/posts', post);

        if(success.value){
            setNewPost(data.value);
            setTotalItems(totalItem.value)
            formData.content = '';
            formData.file = '';
            console.log('Post with file')
            console.log('this is post state', postState.value.posts)
            Toast.fire({
                icon: 'success',
                title: 'Post is successfully created!'
            })
            success.value = null;
        }
       
        if(error.value){
            Toast.fire({
                icon: 'error',
                title: `${error.value}`
            })
            error.value = null;
        }
    }
  
}



const dialog = ref(false)
</script>
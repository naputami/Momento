<template>
    <v-app>
        <NavigationBar />

        <v-container class="pt-16">
            <h1 class="text-center mt-4">Leaderboard</h1>
            <v-table class="mt-8 mb-4">
                <thead>
                    <tr>
                        <th class="text-left">
                            Rank
                        </th>
                        <th class="text-left">
                        Username
                        </th>
                        <th class="text-left">
                        Total Posts
                        </th>
                    </tr>
                </thead>
                <tbody>
                <tr
                    v-for="item in paginatedData"
                    :key="item.id"
                >
                    <td>{{ countPostData.indexOf(item) + 1 }}</td>
                    <td>{{ item.username }}</td>
                    <td>{{ item.countPosts }}</td>
                </tr>
                </tbody>
            </v-table>
            <div class="text-center">
                <v-pagination
                v-model="page"
                :length="Math.ceil(countPostData.length / itemPerPage)"
                :total-visible="4"
                ></v-pagination>
            </div>
        </v-container>
    </v-app>
</template>

<script setup>
import { useFetch } from '../compostable/post';
import { onMounted, ref, computed } from 'vue';
import NavigationBar from "../components/NavigationBar.vue";

const {fetchCountPosts, data} = useFetch();
const countPostData = ref([]);
const page = ref(1);
const itemPerPage = ref(5);

onMounted(async () => {
    await fetchCountPosts();
    countPostData.value = data.value;
})

const paginatedData = computed(() => {
    const start = (page.value - 1) * itemPerPage.value;
    const end = start + itemPerPage.value;
    return countPostData.value.slice(start, end);
})

</script>
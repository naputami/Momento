import axios from "axios";

const postApi = axios.create({
  withCredentials: true
});

postApi.interceptors.request.use(
    (config) => {
        const accessToken = localStorage.getItem('accessToken');
        if (accessToken) {
          config.headers.Authorization = `Bearer ${accessToken}`;
        }
        return config;
      },
      (error) => {
        return Promise.reject(error);
      }
)

postApi.interceptors.response.use(
    (response) => {
        return response;
      },
      async (error) => {
        const originalRequest = error.config;
        if (error.response.status === 401 && !originalRequest._retry) {
          originalRequest._retry = true;
        try {
          const refreshToken = localStorage.getItem('refreshToken');
          const response = await axios.post('/api/auth/refresh', null, {
              headers:{
              'Authorization': `Bearer ${refreshToken}`
          }});
          const newAccessToken = response.data.accessToken;
          localStorage.setItem('accessToken', newAccessToken);
          originalRequest.headers.Authorization = `Bearer ${newAccessToken}`;
          return postApi(originalRequest);
        } catch (refreshError) {
          console.error('Token refresh failed', refreshError);
        }}  
        return Promise.reject(error);
      }
)

export default postApi;
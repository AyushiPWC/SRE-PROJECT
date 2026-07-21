import api from "../api/axios";


const register = async (userData) => {

    const response = await api.post(
        "/auth/register",
        userData
    );

    return response.data;
};


const login = async (credentials) => {

    const formData = new URLSearchParams();

    formData.append(
        "username",
        credentials.email
    );

    formData.append(
        "password",
        credentials.password
    );

    const response = await api.post(
        "/auth/login",
        formData,
        {
            headers: {
                "Content-Type":
                    "application/x-www-form-urlencoded"
            }
        }
    );

    return response.data;
};


const logout = () => {

    localStorage.removeItem("token");

};


const authService = {
    register,
    login,
    logout
};


export default authService;
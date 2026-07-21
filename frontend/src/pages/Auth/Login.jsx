import { useState } from "react";
import {
    useNavigate,
    useLocation
} from "react-router-dom";

import authService from "../../services/authService";
import { useAuth } from "../../context/AuthContext";


function Login() {

    const { login } = useAuth();

    const navigate = useNavigate();
    const location = useLocation();

    const [form, setForm] = useState({
        email: "",
        password: ""
    });

    const [loading, setLoading] = useState(false);
    const [error, setError] = useState("");


    const handleChange = (e) => {

        const { name, value } = e.target;

        setForm((previousForm) => ({
            ...previousForm,
            [name]: value
        }));

        setError("");
    };


    const handleSubmit = async (e) => {

        e.preventDefault();

        setLoading(true);
        setError("");

        try {

            const data = await authService.login(form);

            login(data.access_token);

            const redirectPath =
                location.state?.from?.pathname || "/dashboard";

            navigate(redirectPath, {
                replace: true
            });

        } catch (error) {

            console.error("Login error:", error);

            const errorMessage =
                error.response?.data?.detail ||
                "Invalid email or password";

            setError(errorMessage);

        } finally {

            setLoading(false);

        }
    };


    return (

        <div>

            <h1>Login</h1>

            {error && (
                <p>
                    {error}
                </p>
            )}

            <form onSubmit={handleSubmit}>

                <div>

                    <label htmlFor="email">
                        Email
                    </label>

                    <input
                        id="email"
                        name="email"
                        type="email"
                        placeholder="Enter your email"
                        value={form.email}
                        onChange={handleChange}
                        autoComplete="email"
                        required
                    />

                </div>

                <div>

                    <label htmlFor="password">
                        Password
                    </label>

                    <input
                        id="password"
                        name="password"
                        type="password"
                        placeholder="Enter your password"
                        value={form.password}
                        onChange={handleChange}
                        autoComplete="current-password"
                        minLength={8}
                        required
                    />

                </div>

                <button
                    type="submit"
                    disabled={loading}
                >
                    {loading ? "Logging in..." : "Login"}
                </button>

            </form>

        </div>
    );
}


export default Login;
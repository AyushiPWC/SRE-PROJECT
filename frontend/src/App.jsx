import AppRoutes from "./routes/Approutes";
import { AuthProvider } from "./context/AuthContext";

function App() {

    return (
        <AuthProvider>
            <AppRoutes />
        </AuthProvider>
    );

}

export default App;
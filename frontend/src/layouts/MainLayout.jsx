import { Outlet } from "react-router-dom";

import Navbar from "../components/common/Navbar";
import Footer from "../components/common/Footer";


function MainLayout() {

    return (

        <>

            <Navbar />

            <main
                style={{
                    minHeight: "80vh",
                    padding: "20px",
                    maxWidth: "1200px",
                    margin: "0 auto"
                }}
            >

                <Outlet />

            </main>

            <Footer />

        </>

    );

}


export default MainLayout;
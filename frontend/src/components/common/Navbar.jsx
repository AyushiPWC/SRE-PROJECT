import { Link, useNavigate } from "react-router-dom";

import { useAuth } from "../../context/AuthContext";


function Navbar() {


    const {
        isAuthenticated,
        logout
    } = useAuth();


    const navigate = useNavigate();



    const handleLogout = () => {

        logout();

        navigate("/");

    };



    return (

        <nav

            style={{

                display: "flex",

                justifyContent: "space-between",

                alignItems: "center",

                padding: "15px 30px",

                borderBottom: "1px solid #ddd",

                backgroundColor: "#f8f9fa"

            }}

        >



            <h2>
                Hotel Booking
            </h2>




            <div

                style={{

                    display: "flex",

                    gap: "15px",

                    alignItems: "center"

                }}

            >



                <Link to="/">
                    Home
                </Link>



                {
                    isAuthenticated ? (


                        <>


                            <Link to="/hotels">

                                Hotels

                            </Link>



                            <Link to="/my-bookings">

                                My Bookings

                            </Link>




                            <Link to="/dashboard">

                                Dashboard

                            </Link>




                            <button

                                onClick={handleLogout}

                                style={{

                                    cursor:"pointer",

                                    padding:"5px 10px"

                                }}

                            >

                                Logout

                            </button>



                        </>


                    ) : (


                        <>


                            <Link to="/login">

                                Login

                            </Link>



                            <Link to="/register">

                                Register

                            </Link>


                        </>


                    )
                }



            </div>



        </nav>

    );

}


export default Navbar;
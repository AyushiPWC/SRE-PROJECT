import {
    BrowserRouter,
    Routes,
    Route
} from "react-router-dom";


import MainLayout from "../layouts/MainLayout";


import Home from "../pages/Home";

import Hotels from "../pages/Hotels/Hotels";

import HotelDetails from "../pages/Hotels/HotelDetails";


import Login from "../pages/Auth/Login";

import Register from "../pages/Auth/Register";


import Dashboard from "../pages/Dashboard/Dashboard";


import Booking from "../pages/Bookings/Booking";

import MyBooking from "../pages/Bookings/MyBooking";


import NotFound from "../pages/NotFound";


import ProtectedRoute from "./ProtectedRoute";



function AppRoutes() {


    return (


        <BrowserRouter>


            <Routes>


                <Route

                    path="/"

                    element={<MainLayout />}

                >



                    {/* Home */}

                    <Route

                        index

                        element={<Home />}

                    />



                    {/* Hotels */}

                    <Route

                        path="hotels"

                        element={<Hotels />}

                    />



                    {/* Hotel Details */}

                    <Route

                        path="hotels/:id"

                        element={

                            <ProtectedRoute>

                                <HotelDetails />

                            </ProtectedRoute>

                        }

                    />



                    {/* Booking */}

                    <Route

                        path="book/:hotelId"

                        element={

                            <ProtectedRoute>

                                <Booking />

                            </ProtectedRoute>

                        }

                    />



                    {/* My Bookings */}

                    <Route

                        path="my-bookings"

                        element={

                            <ProtectedRoute>

                                <MyBooking />

                            </ProtectedRoute>

                        }

                    />



                    {/* Dashboard */}

                    <Route

                        path="dashboard"

                        element={

                            <ProtectedRoute>

                                <Dashboard />

                            </ProtectedRoute>

                        }

                    />



                    {/* Auth */}

                    <Route

                        path="login"

                        element={<Login />}

                    />


                    <Route

                        path="register"

                        element={<Register />}

                    />



                </Route>



                {/* 404 */}

                <Route

                    path="*"

                    element={<NotFound />}

                />


            </Routes>


        </BrowserRouter>


    );


}


export default AppRoutes;
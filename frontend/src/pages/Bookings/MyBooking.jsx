import { useEffect, useState } from "react";

import bookingService from "../../services/bookingService";


function MyBooking() {


    const [bookings, setBookings] = useState([]);

    const [loading, setLoading] = useState(true);



    useEffect(() => {

        loadBookings();

    }, []);



    const loadBookings = async () => {


        try {

            const data =
                await bookingService.getMyBookings();


            setBookings(data);


        }

        catch(error) {


            console.error(
                "Failed to load bookings",
                error
            );


        }

        finally {

            setLoading(false);

        }


    };



    const handleCancel = async (bookingId) => {


        const confirmCancel =
            window.confirm(
                "Are you sure you want to cancel this booking?"
            );


        if(!confirmCancel){

            return;

        }



        try {


            await bookingService.cancelBooking(
                bookingId
            );


            alert(
                "Booking cancelled successfully"
            );


            loadBookings();


        }

        catch(error) {


            console.error(
                "Cancel booking failed",
                error
            );


            alert(
                "Unable to cancel booking"
            );


        }


    };



    if(loading){

        return (

            <h2>
                Loading bookings...
            </h2>

        );

    }



    return (

        <div
            style={{
                padding:"20px",
                maxWidth:"900px",
                margin:"auto"
            }}
        >


            <h1>
                My Bookings
            </h1>



            {
                bookings.length === 0 ? (

                    <p>
                        No bookings found.
                    </p>

                ) : (


                    bookings.map((booking)=>(


                        <div

                            key={booking.id}

                            style={{
                                border:"1px solid #ccc",
                                padding:"20px",
                                marginBottom:"20px",
                                borderRadius:"10px"
                            }}

                        >


                            <h3>
                                Booking ID: {booking.id}
                            </h3>



                            <p>
                                Hotel ID:
                                {" "}
                                {booking.hotel_id}
                            </p>



                            <p>
                                Check In:
                                {" "}
                                {booking.check_in_date}
                            </p>



                            <p>
                                Check Out:
                                {" "}
                                {booking.check_out_date}
                            </p>



                            <p>
                                Total Price:
                                {" "}
                                ₹{booking.total_price}
                            </p>



                            <p>
                                Status:
                                {" "}
                                {booking.status}
                            </p>




                            {
                                booking.status !== "CANCELLED"
                                &&
                                booking.status !== "CHECKED_OUT"
                                &&
                                (

                                    <button

                                        onClick={() =>
                                            handleCancel(
                                                booking.id
                                            )
                                        }

                                    >

                                        Cancel Booking

                                    </button>

                                )
                            }



                        </div>


                    ))

                )
            }



        </div>

    );

}


export default MyBooking;
import { useState } from "react";

import { useParams, useNavigate } from "react-router-dom";

import bookingService from "../../services/bookingService";


function Booking() {


    const { hotelId } = useParams();

    const navigate = useNavigate();


    const [form, setForm] = useState({

        check_in_date: "",

        check_out_date: ""

    });



    const handleChange = (e) => {

        setForm({

            ...form,

            [e.target.name]: e.target.value

        });

    };



    const handleSubmit = async (e) => {

        e.preventDefault();


        try {


            await bookingService.createBooking(

                hotelId,

                form.check_in_date,

                form.check_out_date

            );


            alert(
                "Booking created successfully"
            );


            navigate("/my-bookings");


        }

        catch(error) {


            console.error(error);


            alert(
                "Booking failed"
            );

        }


    };



    return (

        <div
            style={{
                maxWidth:"500px",
                margin:"30px auto"
            }}
        >

            <h1>
                Book Hotel
            </h1>


            <form
                onSubmit={handleSubmit}
            >


                <label>
                    Check In Date
                </label>


                <br/>


                <input

                    type="date"

                    name="check_in_date"

                    value={form.check_in_date}

                    onChange={handleChange}

                    required

                />



                <br/><br/>



                <label>
                    Check Out Date
                </label>


                <br/>



                <input

                    type="date"

                    name="check_out_date"

                    value={form.check_out_date}

                    onChange={handleChange}

                    required

                />



                <br/><br/>



                <button>

                    Confirm Booking

                </button>


            </form>


        </div>

    );

}


export default Booking;
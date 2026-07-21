import { useEffect, useState } from "react";
import { useParams, useNavigate } from "react-router-dom";

import hotelService from "../../services/hotelService";


function HotelDetails() {

    const { id } = useParams();

    const navigate = useNavigate();


    const [hotel, setHotel] = useState(null);

    const [loading, setLoading] = useState(true);



    useEffect(() => {

        loadHotel();

    }, []);



    const loadHotel = async () => {

        try {

            const data =
                await hotelService.getHotelById(id);

            setHotel(data);

        }

        catch (error) {

            console.error(error);

        }

        finally {

            setLoading(false);

        }

    };



    if (loading) {

        return <h2>Loading...</h2>;

    }



    if (!hotel) {

        return <h2>Hotel not found.</h2>;

    }



    const handleBooking = () => {

        navigate(`/book/${hotel.id}`);

    };



    return (

        <div
            style={{
                maxWidth: "700px",
                margin: "30px auto",
                padding: "20px",
                border: "1px solid #ddd",
                borderRadius: "10px"
            }}
        >

            <h1>
                {hotel.name}
            </h1>


            <p>
                <strong>Location:</strong> {hotel.location}
            </p>


            <p>
                <strong>Price:</strong> ₹{hotel.price_per_night}
            </p>


            <p>
                <strong>Available Rooms:</strong> {hotel.available_rooms}
            </p>


            <p>
                <strong>Rating:</strong> ⭐ {hotel.rating}
            </p>


            <p>
                <strong>Description:</strong>
            </p>


            <p>
                {hotel.description}
            </p>



            {
                hotel.image_url && (

                    <img

                        src={hotel.image_url}

                        alt={hotel.name}

                        width="100%"

                    />

                )
            }



            <br />
            <br />



            <button

                onClick={handleBooking}

                style={{
                    padding:"10px 20px",
                    cursor:"pointer"
                }}

            >

                Book Now

            </button>


        </div>

    );

}


export default HotelDetails;
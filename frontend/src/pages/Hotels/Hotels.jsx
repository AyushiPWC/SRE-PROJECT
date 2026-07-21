import { useEffect, useState } from "react";

import { useNavigate } from "react-router-dom";

import hotelService from "../../services/hotelService";


function Hotels() {

    const [hotels, setHotels] = useState([]);

    const navigate = useNavigate();


    useEffect(() => {

        loadHotels();

    }, []);


    const loadHotels = async () => {

        try {

            const data = await hotelService.getHotels();

            setHotels(data);

        }

        catch (error) {

            console.error(error);

        }

    };


    return (

        <div
            style={{
                maxWidth: "900px",
                margin: "30px auto"
            }}
        >

            <h1>
                Hotels
            </h1>

            {

                hotels.length === 0 ?

                    (

                        <p>No hotels found.</p>

                    )

                    :

                    (

                        hotels.map((hotel) => (

                            <div
                                key={hotel.id}
                                style={{
                                    border: "1px solid #ddd",
                                    borderRadius: "10px",
                                    padding: "20px",
                                    marginBottom: "20px"
                                }}
                            >

                                <h2>
                                    {hotel.name}
                                </h2>

                                <p>
                                    📍 {hotel.location}
                                </p>

                                <p>
                                    💰 ₹{hotel.price_per_night} / Night
                                </p>

                                <p>
                                    ⭐ {hotel.rating}
                                </p>

                                <button
                                    onClick={() =>
                                        navigate(`/hotels/${hotel.id}`)
                                    }
                                >
                                    View Details
                                </button>

                            </div>

                        ))

                    )

            }

        </div>

    );

}

export default Hotels;
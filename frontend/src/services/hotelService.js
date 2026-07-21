import api from "../api/axios";

// Get all hotels
const getHotels = async () => {

    const response = await api.get("/hotels/");

    return response.data;

};


// Get hotel by ID
const getHotelById = async (id) => {

    const response = await api.get(`/hotels/${id}`);

    return response.data;

};


// Search hotels
const searchHotels = async (location) => {

    const response = await api.get(`/hotels/search/${location}`);

    return response.data;

};


const hotelService = {

    getHotels,

    getHotelById,

    searchHotels

};


export default hotelService;
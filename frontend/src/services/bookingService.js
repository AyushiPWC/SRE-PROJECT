import api from "../api/axios";


// =====================================
// Create Booking
// POST /api/v1/bookings/
// =====================================

const createBooking = async (
    hotelId,
    checkInDate,
    checkOutDate
) => {

    const response = await api.post(
        "/bookings/",
        {
            hotel_id: Number(hotelId),
            check_in_date: checkInDate,
            check_out_date: checkOutDate
        }
    );


    return response.data;

};



// =====================================
// Get My Bookings
// GET /api/v1/bookings/my-bookings
// =====================================

const getMyBookings = async () => {

    const response = await api.get(
        "/bookings/my-bookings"
    );


    return response.data;

};



// =====================================
// Get Booking By ID
// GET /api/v1/bookings/{booking_id}
// =====================================

const getBooking = async (bookingId) => {

    const response = await api.get(
        `/bookings/${bookingId}`
    );


    return response.data;

};



// =====================================
// Cancel Booking
// PUT /api/v1/bookings/{booking_id}/cancel
// =====================================

const cancelBooking = async (bookingId) => {

    const response = await api.put(
        `/bookings/${bookingId}/cancel`
    );


    return response.data;

};



// =====================================
// Update Booking Status
// PUT /api/v1/bookings/{booking_id}/status
// =====================================

const updateBookingStatus = async (
    bookingId,
    status
) => {

    const response = await api.put(
        `/bookings/${bookingId}/status`,
        {
            status: status
        }
    );


    return response.data;

};



// Export Service

const bookingService = {

    createBooking,

    getMyBookings,

    getBooking,

    cancelBooking,

    updateBookingStatus

};


export default bookingService;
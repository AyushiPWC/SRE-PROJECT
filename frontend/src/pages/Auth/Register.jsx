import {
    useState
} from "react";

import authService from "../../services/authService";


function Register(){

    const [form,setForm] = useState({
        name:"",
        email:"",
        password:""
    });



    const handleChange=(e)=>{

        setForm({
            ...form,
            [e.target.name]:
            e.target.value
        });

    };



    const handleSubmit=async(e)=>{

        e.preventDefault();


        try{

            await authService.register(form);

            alert(
                "Registration successful"
            );


        }
        catch(error){

            alert(
                "Registration failed"
            );

        }

    };



    return (

        <div>

            <h1>
                Register
            </h1>


            <form onSubmit={handleSubmit}>


                <input
                name="name"
                placeholder="Name"
                onChange={handleChange}
                />


                <input
                name="email"
                placeholder="Email"
                onChange={handleChange}
                />


                <input
                name="password"
                placeholder="Password"
                type="password"
                onChange={handleChange}
                />


                <button>
                    Register
                </button>


            </form>


        </div>

    );

}


export default Register;
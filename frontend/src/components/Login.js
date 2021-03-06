import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { Row, Form, Button, Container} from "react-bootstrap";
import axios from "axios";

const Login = () => {

    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const history = useNavigate();
    const [userInfo, setUserInfo] = useState();

    const onSubmit = e => {
        e.preventDefault();

        const data = {
            Email: email,
            Password: password
        };

        axios
        .post('http://localhost:5000/login', data)
        .then(res => {
            setEmail('')
            setPassword('')

            setUserInfo(res.data.User_ID)
            //window.location = "/homepage/" + userInfo
        })
        .catch(err => {
            console.log("Error in Login!");
        })
    }

    return(
        <>
            <Container>
                <Row>
                    <h1><b>Login</b></h1>
                    <Form onSubmit={onSubmit}>
                        <Form.Group className="mb-3" controlId="formBasicEmail">
                            <Form.Label>Email address</Form.Label>
                            <Form.Control 
                                type="email"
                                placeholder="Enter email"
                                value={email}
                                onChange={e => setEmail(e.target.value)}    
                            />
                        </Form.Group>

                        <Form.Group className="mb-3" controlId="formBasicPassword">
                            <Form.Label>Password</Form.Label>
                            <Form.Control
                                type="password"
                                placeholder="Password" 
                                value={password}
                                onChange={e => setPassword(e.target.value)}
                            />
                        </Form.Group>
                        <Button variant="primary" type="submit">
                            Submit
                        </Button>
                    </Form>
                </Row>
            </Container>
        </>
    )

}

export default Login;
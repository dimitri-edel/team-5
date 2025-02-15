import React from "react";
import Col from "react-bootstrap/Col";
import Row from "react-bootstrap/Row";
import Image from "react-bootstrap/Image";
import styles from "../styles/about.module.css";
import appStyles from "../App.module.css";
import Container from "react-bootstrap/Container";
const AboutPage = () => {
    return (
        <Container className={styles.AboutContainer}>
            <Row>
                <Col md={6} className={`my-auto d-md-block p-2`}>
                    <div className={styles.Info}>
                        <h1>About Us</h1>
                        <p>We are The CodeInstitute-February-Hakathon's Competitors</p>
                        <p>
                        The Goal of this project is to provide a platform where a user could easily look for and find specific persons.
                        We have tried our best to follow the criteria set out by the hackathon facilitators and incorporating the hard work, 
                        skills and abilities of each team member while enjoying the process of learning to develop new and unique software.
                        </p>
                        <h3>Our mission</h3>
                        <p>
                            Encouraging people to meet others, those that share common interests.
                        </p>
                    </div>
                </Col>
                <Col md={6} className={`my-auto d-none d-md-block p-2`}>
                /**
                Add Image 
                    <Image
                        className={`${appStyles.FillerImage}`}
                        src={
                            ""
                        }
                    />
                    */ 
                </Col>
            </Row>
        </Container>
    );
};
export default AboutPage;
import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import About from './about';
import Course from './course';
import CourseList from './courseList';
import { UserProps } from './utils';
import Footer from './footer';
import Contact from './contact';

declare global {
    interface Window {
        r4r: {
            staticUrl: string,
            baseUrl: string,
            currentUser: UserProps
        }
    }
}


export default function App() {
    return <Router>
        <div className='container'>
            <div className="my-4">
                <Routes>
                    <Route path='/' element={<CourseList />} />
                    <Route path='/about' element={<About/>} />
                    <Route path='/contact' element={(<Contact/>)} />
                    <Route path='/course/:courseId' element={<Course/>} />
                </Routes>
            </div>
        </div>
        <Footer />
    </Router>;
};
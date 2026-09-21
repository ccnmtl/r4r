import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import CourseList from './courseList';
import Course from './course';
import { UserProps } from './utils';

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
        <Routes>
            <Route path="/" element={<CourseList/>} />
            <Route path="/course/:courseId" element={<Course/>} />
        </Routes>
    </Router>;
};
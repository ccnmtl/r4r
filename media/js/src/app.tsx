import React from 'react';
import {
    BrowserRouter as Router, Route, Routes, Outlet
} from 'react-router-dom';
import About from './about';
import CourseList from './courseList';
import { authUser, generateNestedRoute, UserProps } from './utils';
import Contact from './contact';
import { rotationRoutes } from './rotation';
import { membersRoutes } from './members';
import Insights from './insights';
import Feedback, {feedbackRoutes} from './feedback';
import StudentDashboard from './studentDashboard';
import StudentRotation from './studentRotation';
import Nav from './nav';

declare global {
    interface Window {
        r4r: {
            staticUrl: string,
            baseUrl: string,
            currentUser: UserProps,
            csrf: string
        }
    }
}

const staff = authUser.is_staff;

const staffRoutes = <Route path='/' element={<Outlet />}>
    <Route index element={<CourseList />} />
    <Route path='course/:courseId' element={<Nav />}>
        <Route index element={<Feedback />} />
        {feedbackRoutes}
        {rotationRoutes}
        {membersRoutes}
        <Route path={'insights'} element={<Insights />} />
        <Route path={'about'} element={<About />} />
        <Route path={'contact'} element={<Contact />} />
    </Route>;
</Route>;

const studentRoutes = generateNestedRoute(
    {path: '/', el: <Nav />},
    [
        {path: 'dashboard', el: <StudentDashboard />},
        {path: 'about', el: <About />},
        {path: 'contact', el: <Contact />},
        {path: 'rotation', el: <StudentRotation />}
    ]
);

export default function App() {
    return <Router>
        <Routes>
            {staff ? staffRoutes : studentRoutes}
        </Routes>
    </Router>;
};
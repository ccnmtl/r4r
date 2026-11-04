import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import About from './about';
import Dashboard from './dashboard';
import CourseList from './courseList';
import { authUser, UserProps } from './utils';
import Footer from './footer';
import Contact from './contact';
import Topbar from './topbar';
import Sidebar from './sidebar';

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

export default function App() {
    return <Router>
        <div className={`d-flex${staff ? '' : ' flex-column'} vh-100`}>
            {staff ? <Sidebar unread={0} /> : <Topbar />}
            <main id='content' className='d-flex flex-column m-0 w-100 h-100'>
                <div className='mb-auto p-4'>
                    <Routes>
                        <Route path='/' element={<CourseList />} />
                        <Route path='/about' element={<About/>} />
                        <Route path='/contact' element={(<Contact/>)} />
                        <Route path='/course/:courseId'
                            element={<Dashboard/>} />
                    </Routes>
                </div>
                <Footer />
            </main>
        </div>
    </Router>;
};
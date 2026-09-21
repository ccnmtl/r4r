import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';
import { CourseProps, authUser } from './utils';


const userId = authUser.id ;
const isStaff = authUser.is_staff;

export default function CourseList() {
    const [courseList, setCourseList] = useState<CourseProps[]>();

    console.log('User ID:', userId);
    useEffect(() => {
        axios.get(`api/user/${userId}/courses/`)
            .then(response => setCourseList(response.data));
    },[]);

    useEffect(() => {
        console.log('Course List', courseList);
    }, [courseList]);

    return <section id='courses'>
        <h1>My Courses</h1>
        {isStaff ? 'You are Staff' : 'You are NOT staff'}
        <div id='course-list' className='list-group'>
            {courseList ?
                (courseList.length > 0) ?
                    courseList.map(
                        (course, i) => {
                            if (course.is_active) {
                                return <Link key={i} to={`course/${course.id}`}
                                    className={`list-group-item
                                        list-group-item-action 
                                        ${i%2 && 'bg-light'}`}
                                >
                                    <div className='row'>
                                        <p className='col-3'>{course.title}</p>
                                        <p className='col-3'>{course.code}</p>
                                        <p className='col-6'>
                                            {course.details ||
                                                <em className='text-secondary'>
                                                    No details</em>}
                                        </p>
                                    </div>
                                </Link>;}})
                    :
                    <div className='list-group-item list-group-item-info'>
                        <p>
                            There are no courses available to you.
                        </p>
                    </div>
                :
                <div className='spinner-border text-secondary' role='status'>
                    <span className='visually-hidden'>Loading...</span>
                </div>
            }
        </div>
    </section>;
};
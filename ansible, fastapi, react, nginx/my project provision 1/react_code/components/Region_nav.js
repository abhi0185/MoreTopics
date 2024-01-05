// Region_nav.js

import React from 'react';
import {
    Nav2,
    NavLink,
    Bars,
    NavMenu,
} from "./css/NavbarElements";

// Functional component
const NavBar = () => {

  return (
    <Nav2>
     <Bars />

	  <NavMenu>
            <NavLink to ="/add_region">Add Region</NavLink>
            <NavLink to ="/update_region">Update Region</NavLink>
            <NavLink to ="/detail_region">View Region</NavLink>
	  </NavMenu>
    </Nav2>
  );
};


export default NavBar;


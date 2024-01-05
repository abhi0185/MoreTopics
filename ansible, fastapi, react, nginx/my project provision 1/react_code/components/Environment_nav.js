// Region_nav.js

import React from 'react';
import {
    Nav2,
    NavLink,
    Bars,
    NavMenu,
} from "./css/NavbarElements";

// Functional component
const EnvBar = () => {

  return (
    <Nav2>
     <Bars />

	  <NavMenu>
            <NavLink to ="/add_new_environment">Add New Environment</NavLink>
            <NavLink to ="/update_environment">Update Environment</NavLink>
            <NavLink to ="/detail_environment">View Environment</NavLink>
	  </NavMenu>
    </Nav2>
  );
};


export default EnvBar;


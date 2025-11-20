"use client ";

import React from "react";

type ButtonProps = {
  children: React.ReactNode;
  variant?: "primary" | "secondary" | "outline";
  size?: "sm" | "md" | "lg";
  className?: string;
} & React.ButtonHTMLAttributes<HTMLButtonElement>;

export default function Button( { 
    // arguments that a button can have 

    children,
    variant = "primary",
    size = "md",
    className = "",
    ...props


} : ButtonProps ){

    let variantClasses = "";

    if(variant === "primary") {
        variantClasses = "bg-blue-600 text-white hover:bg-blue-700";
    }
    else if(variant === "secondary") {
        variantClasses = "bg-gray-200 text-gray-900 hover:bg-gray-300";
    }
    else if(variant === "outline") {
        variantClasses = "border border-gray-300 text-gray-900 hover:bg-gray-100";
    }

    let sizeClasses = ""

    if (size === "sm") sizeClasses = "px-2 py-1 text-sm";
    if (size === "md") sizeClasses = "px-4 py-2";
    if (size === "lg") sizeClasses = "px-6 py-3 text-lg";



    return (

        <button
            className={`rounded font-medium transition ${variantClasses} ${sizeClasses} ${className}`}
            {...props}
        
        >
            {children}
        </button>
    )
}
import React, { useEffect } from 'react';
import './ChatBot.css';

const ChatBot = () => {
  useEffect(() => {
    // Load the Botpress webchat script
    const script1 = document.createElement('script');
    script1.src = "https://cdn.botpress.cloud/webchat/v2.2/inject.js";
    script1.async = true;
    document.body.appendChild(script1);

    // Load the configuration script
    const script2 = document.createElement('script');
    script2.src = "https://files.bpcontent.cloud/2025/01/11/03/20250111031318-1JZ61EFU.js";
    script2.async = true;
    document.body.appendChild(script2);

    // Cleanup function to remove scripts when component unmounts
    return () => {
      document.body.removeChild(script1);
      document.body.removeChild(script2);
    };
  }, []); // Empty dependency array means this runs once on mount

  return (
    <div id="botpress-webchat" className="chatbot-container" />
  );
};

export default ChatBot; 
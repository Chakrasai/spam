import React from 'react';

function Spamemail({ result }) {
  const isSpam = result === 'Spam';

  return (
    <div>
      {isSpam ? (
        <h1>It is a Spam email</h1>
      ) : (
        <h1>It is not a Spam email</h1>
      )}
    </div>
  );
}

export default Spamemail;



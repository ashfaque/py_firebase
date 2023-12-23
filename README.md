# Firebase with Python3

- Goto [console of firebase](https://console.firebase.google.com/)
- Then goto your project's `Project settings`
- Then click no `Service Accounts`
- Choose `Python` and `Generate new private key`
- Save that key somewhere and we will be using that key path to to authenticate multiple Firebase features, such as Database, Storage and Auth, programmatically via the unified Admin SDK.


```sh
conda activate py_fbase_env
```
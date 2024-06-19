{
  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-24.05";
  };

  outputs = { self, nixpkgs }:
    let
      system = "x86_64-linux";
      pkgs = import nixpkgs { inherit system; };
    in
      {
        devShells.${system}.default = pkgs.mkShell {
          nativeBuildInputs = with pkgs; [ pkg-config ];
          buildInputs = with pkgs; [
            # Nix env
            nil
            nixpkgs-fmt

            # C env
            stdenv.cc

            # Python
            python310
            python310Packages.pip

            # SVG to PNG
            cairo
            (builtins.trace "${cairo}/lib" cairo)
          ];

          shellHook = with pkgs; ''
            export LD_LIBRARY_PATH="${lib.makeLibraryPath [ stdenv.cc.cc cairo ]}:$LD_LIBRARY_PATH"
            source .venv/bin/activate
          '';
        };
      };
}
